package br.com.hackathon.selfservice

sealed class SelfServiceMessage(val content: String)

data class UserMessage(val message: String) : SelfServiceMessage(message)
data class ServerMessage(val message: String, val imageUrl: List<String>) : SelfServiceMessage(message)
