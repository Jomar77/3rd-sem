public class TestCaesar {
    public static void main(String[] args) {
        CaesarCIpher c = new CaesarCIpher();
        c.setPlaintext("hello world");
        c.setKey(4);
        c.encrypt();

        System.out.println("plaintext: " + c.getPlaintext());
        
        CaesarCIpher c2 = new CaesarCIpher("hello world", 4);
        c2.encrypt();
        System.out.println("Ciphertext: " + c2.getCiphertext());

        CaesarCIpher c3 = new CaesarCIpher();
        c3.encrypt("eclipse", 8);
        System.out.println( c3.getCiphertext());

        CaesarCIpher c4 = new CaesarCIpher();
        System.out.println(c4.encryptS("structure", 6));

        c.setCiphertext("nslrc");
        c.setKey(4);
        System.out.println(c.decrypt());
    }
}
