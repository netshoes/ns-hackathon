package br.com.hackathon.selfservice

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.inputmethod.EditorInfo
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.functions.FirebaseFunctions
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.*
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.lang.Exception
import java.util.*
import kotlin.coroutines.CoroutineContext
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private val adapter = MessagesAdapter()
    private val webservice by lazy {
//        val serviceUrl = "https://demo1817160.mockable.io/"
        val serviceUrl = "https://dialogflow.googleapis.com/"
        Retrofit.Builder()
            .baseUrl(serviceUrl)
            .client(
                OkHttpClient.Builder().addInterceptor(
                    HttpLoggingInterceptor().apply { level = HttpLoggingInterceptor.Level.BODY }
                ).build()
            )
            .addConverterFactory(GsonConverterFactory.create(GsonBuilder().create()))
            .build().create(Webservice::class.java)
    }

    private val prodImages = listOf(
        "https://static.netshoes.com.br/produtos/kit-nutri-whey-protein-3x-907-g-refi-integralmedica/99/252-7206-799/252-7206-799_zoom1.jpg",
        "https://static.netshoes.com.br/produtos/thermogenic-120-caps-probiotica/01/168-9283-001/168-9283-001_zoom1.jpg",
        "https://static.netshoes.com.br/produtos/massa-17500-3-kg-refil-max-titanium/24/A05-0022-E24/A05-0022-E24_zoom1.jpg",
        "https://static.netshoes.com.br/produtos/amino-hard-10-200g-integralmedica/56/252-7906-456/252-7906-456_detalhe1.jpg?resize=280:280"
    )

    private val functions by lazy {
        FirebaseFunctions.getInstance()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView.layoutManager = LinearLayoutManager(this, LinearLayoutManager.VERTICAL,
            false)
        recyclerView.adapter = adapter
        recyclerView.setHasFixedSize(false)

        editText.setOnEditorActionListener { v, actionId, event ->
            return@setOnEditorActionListener when (actionId) {
                EditorInfo.IME_ACTION_SEND -> {
                    sendMessage()
                    true
                }
                else -> false
            }
        }

        floatingActionButton.setOnClickListener {
            sendMessage()
        }

    }

    private fun sendMessage() {
        val message = editText.text.toString()
        addNewMessage(UserMessage(message))
        CoroutineScope(Dispatchers.IO).launch {
//            send2("enviando dados")
//            send("adasdasd")
            sendDialog(QueryInput(QueryText(message)))
        }
        editText.text.clear()
    }

    private suspend fun sendDialog(queryInput: QueryInput) {
//        val sendDialogFlow = webservice.sendDialogFlow(UUID.randomUUID().toString(), DialogRequest(queryInput))
        val sendDialogFlow = webservice.sendDialogFlow("1234444666", DialogRequest(queryInput))
        withContext(Dispatchers.Main) {
            if (sendDialogFlow.isSuccessful) {
                sendDialogFlow.body()?.let {
                    addNewMessage(ServerMessage(it.queryResult?.fulfillmentText ?: "Fullfilment not available", prodImages))
                }
            } else {
                Snackbar.make(rootView, "Error sending message", Snackbar.LENGTH_SHORT).show()
                Log.e("ERROR", sendDialogFlow.errorBody()?.string() ?: "")
            }
        }
    }

    private suspend fun send(message: String) {
        val serverResponse = webservice.sendMessage(message)
        withContext(Dispatchers.Main) {
            if (serverResponse.isSuccessful) {
                serverResponse.body()?.let {
                    addNewMessage(ServerMessage(it.message, prodImages))
                }
            } else {
                Snackbar.make(rootView, "Error sending message", Snackbar.LENGTH_SHORT).show()
                Log.e("ERROR", serverResponse.errorBody()?.string() ?: "")
            }
        }
    }

    private  suspend fun send2(message: String) {
        postaLa(message)
//        withContext(Dispatchers.Main) {
//            if (serverResponse.isSuccessful) {
//                serverResponse.body()?.let {
//                    addNewMessage(ServerMessage(it.message))
//                }
//            } else {
//                Snackbar.make(rootView, "Error sending message", Snackbar.LENGTH_SHORT).show()
//            }
//        }
    }

    private fun addNewMessage(newMessage: SelfServiceMessage) {
        adapter.addMessage(newMessage)
        recyclerView.scrollToPosition(adapter.itemCount - 1)
    }

    private fun postaLa(text: String){
        val data = hashMapOf(
            "text" to text,
            "language" to "pt-BR"
        )

        functions
            .getHttpsCallable("postaLa")
            .call(data)
            .continueWith {
                val result = it.result?.data as String
                Log.d("LOGANDO", result)
            }
    }
}
