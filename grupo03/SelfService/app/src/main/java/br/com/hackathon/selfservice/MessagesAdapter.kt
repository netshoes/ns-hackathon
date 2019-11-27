package br.com.hackathon.selfservice

import android.graphics.Color
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.squareup.picasso.Callback
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.cell_server_message.view.*
import kotlinx.android.synthetic.main.cell_user_message.view.*
import kotlinx.android.synthetic.main.cell_user_message.view.message_textView
import java.lang.Exception

class MessagesAdapter : RecyclerView.Adapter<MessagesAdapter.MessagesViewHolder>() {

    private val messages = mutableListOf<SelfServiceMessage>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MessagesViewHolder {
        val layoutResource = if (viewType == 0) {
            R.layout.cell_user_message
        } else {
            R.layout.cell_server_message
        }

        val view = LayoutInflater.from(parent.context).inflate(
            layoutResource,
            parent,
            false
        )
        return MessagesViewHolder(view)
    }

    override fun getItemViewType(position: Int): Int {
        return when (messages[position]) {
            is UserMessage -> 0
            is ServerMessage -> 1
        }
    }

    override fun getItemCount(): Int = messages.size

    override fun onBindViewHolder(holder: MessagesViewHolder, position: Int) {
        holder.bind(messages[position])
    }

    fun addMessage(message: SelfServiceMessage) {
        messages.add(message)
        notifyItemInserted(messages.size - 1)
    }

    class MessagesViewHolder(private val view: View) : RecyclerView.ViewHolder(view) {
        fun bind(message: SelfServiceMessage) {
            with(view.message_textView) {
                text = message.content
            }

            if (message is ServerMessage ){
                if (message.message.contains("interesse:") && message.imageUrl.isNotEmpty()) {
                    Picasso.get().load(message.imageUrl[0]).into(view.productImage)
                    Picasso.get().load(message.imageUrl[1]).into(view.productImage2)
                    Picasso.get().load(message.imageUrl[2]).into(view.productImage3)
                    Picasso.get().load(message.imageUrl[3]).into(view.productImage4)

                    view.productImage.visibility = View.VISIBLE
                    view.productImage2.visibility = View.VISIBLE
                    view.productImage3.visibility = View.VISIBLE
                    view.productImage4.visibility = View.VISIBLE

                }else{
                    view.productImage.visibility = View.GONE
                    view.productImage2.visibility = View.GONE
                    view.productImage3.visibility = View.GONE
                    view.productImage4.visibility = View.GONE
                }
            }
        }
    }

}

class PicassoCallback(val view: View) : Callback {
    override fun onSuccess() {
        view.visibility = View.VISIBLE
    }

    override fun onError(e: Exception?) {
        view.visibility = View.GONE
    }

}