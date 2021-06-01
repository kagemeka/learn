fun sendMessageToClient(
        client: Client?, message: String?, mailer: Mailer
){
   if (client == null || message == null) return
}

class Client (val personalInfo: PersonalInfo?)
class PersonalInfo (val email: String?)
interface Mailer {
    fun sendMessage(email: String, message: String)
}