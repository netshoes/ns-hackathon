package br.com.hackathon.selfservice

import androidx.annotation.Keep
import com.google.gson.annotations.SerializedName

@Keep
data class DialogRequest(
    @SerializedName("query_input") val query: QueryInput
)

@Keep
data class QueryInput(
    @SerializedName("text") var text: QueryText
)

@Keep
data class QueryText (
    @SerializedName("text") var text: String,
    @SerializedName("language_code") var language: String = "pt-BR"
)
