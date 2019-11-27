package br.com.hackathon.selfservice


import com.google.gson.annotations.SerializedName

data class DialogResponse(
    @SerializedName("queryResult")
    val queryResult: QueryResult? = QueryResult(),
    @SerializedName("responseId")
    val responseId: String? = ""
) {
    data class QueryResult(
        @SerializedName("action")
        val action: String? = "",
        @SerializedName("diagnosticInfo")
        val diagnosticInfo: DiagnosticInfo? = DiagnosticInfo(),
        @SerializedName("fulfillmentMessages")
        val fulfillmentMessages: List<FulfillmentMessage?>? = listOf(),
        @SerializedName("fulfillmentText")
        val fulfillmentText: String? = "",
        @SerializedName("intent")
        val intent: Intent? = Intent(),
        @SerializedName("intentDetectionConfidence")
        val intentDetectionConfidence: Double? = 0.0,
        @SerializedName("languageCode")
        val languageCode: String? = "",
        @SerializedName("outputContexts")
        val outputContexts: Any? = null,
        @SerializedName("parameters")
        val parameters: Parameters? = Parameters(),
        @SerializedName("queryText")
        val queryText: String? = ""
    ) {
        class DiagnosticInfo(
        )

        data class FulfillmentMessage(
            @SerializedName("text")
            val text: Text? = Text()
        ) {
            data class Text(
                @SerializedName("text")
                val text: List<String?>? = listOf()
            )
        }

        data class Intent(
            @SerializedName("displayName")
            val displayName: String? = "",
            @SerializedName("name")
            val name: String? = ""
        )

        data class Parameters(
            @SerializedName("date")
            val date: String? = "",
            @SerializedName("duration")
            val duration: String? = "",
            @SerializedName("guests")
            val guests: Int? = 0,
            @SerializedName("location")
            val location: String? = "",
            @SerializedName("time")
            val time: String? = ""
        )
    }
}