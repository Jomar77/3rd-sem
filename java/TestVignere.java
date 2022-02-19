public class TestVignere {
    public static void main(String[] args) {
        VignereCipher vignere1=new VignereCipher();
        vignere1.setPlaintextAndKey("I love java", "hello");
        vignere1.encrypt(); 
        System.out.println(vignere1.getCiphertext()); 
        vignere1.decrypt();
        System.out.println(vignere1.getDecrypted()); }// end of main
}
