package br.com.hackathon.selfservice

import retrofit2.Response
import retrofit2.http.*

interface Webservice {

    @POST("/support")
    suspend fun sendMessage(@Body message: String) : Response<ServerResponse>

    @POST("v2/projects/hackathon-03/agent/sessions/{sessionId}:detectIntent")
    @Headers("Authorization: Bearer ya29.c.Kl6RB3fqIwjCBru_T-CQ6OH_9mEQVtLW_7nF3xgU51Z4GQvsy2aT7ftPWR9_KkCvoMXykvd1JCMebnbrZgtK3tHUTJbCO4fI7Zcswnj4M8fzlZOxvoaCWEVdP5hI_Ktd")
    suspend fun sendDialogFlow(@Path("sessionId") sessionId: String, @Body dialogRequest: DialogRequest) : Response<DialogResponse>

}
