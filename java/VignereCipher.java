public class VignereCipher {
    private String plaintext = "", decrypted = "", ciphertext = "h", key = "";

    /** creators - constructors */
    public VignereCipher() {
    }

    public VignereCipher(String plaintext, String key) {
        this.plaintext = plaintext;
        this.key = key;
    }
    
    /** setters - mutators */

    public void setPlaintextAndKey(String plaintext, String key) {
        this.plaintext = plaintext;
        this. key = key; 
    }

    /** getters - accessors */
    public String getCiphertext() {
        return ciphertext;
    }

    public String getPlaintext() {
        return plaintext;
    }

    public String getKey() {
        return key;
    }

    public String getDecrypted() {
        return decrypted;
    }

    public void encrypt() {
        ciphertext = "";
        char val = '\0';
        plaintext = plaintext.toUpperCase();
        key = key.toUpperCase();
        for (int a = 0, b = 0; a < plaintext.length(); a++) {
            char ch = plaintext.charAt(a);
            if (ch < 'A' || ch > 'Z') {
                ciphertext += ch;
            } else {
                ciphertext += (char)((ch + key.charAt(b)-2 * 'A') % 26 + 'A');
                b = ++b % key.length();
            } // end of if
        } // end of loop
    }// end of encrypt

    public String encrypt( String plaintext, String key){
        setPlaintextAndKey(plaintext, key);
        encrypt();
        return getCiphertext();
    }

    public void decrypt() {
        char val = '\0';
        ciphertext = ciphertext.toUpperCase();
        key = key.toUpperCase();
        for (int a = 0, b = 0; a < ciphertext.length(); a++) {
            char ch = ciphertext.charAt(a);
            if (ch < 'A' || ch > 'Z') {
                decrypted += ch;
            } else {
               decrypted += (char) ((ch - key.charAt(b) + 26) % 26 + 'A');
                b = ++b % key.length();
            } // end of if
        } // end of loop
    }
}// end of class
