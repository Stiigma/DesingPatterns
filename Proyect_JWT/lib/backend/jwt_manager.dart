class JwtManeger(){
    
    //unique Instance by Singleton Patron
    static final JwtManeger _instance = 



    //Contructor private w dart
    JwtManeger._instance(); 

    factory JwtManeger(){
        return _instance;
    }


    //method generative JWT

    String GenerativeToken(String userId){
        final jwt = JWT({'sub': userId}, issuer: 'app');
        return jwt.sing(SecretKey('IgrisGod22!'));
    }
}