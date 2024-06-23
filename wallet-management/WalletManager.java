// WalletManager.java
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.util.HashMap;
import java.util.Map;

public class WalletManager {
    private Map<String, KeyPair> wallets;

    public WalletManager() {
        this.wallets = new HashMap<>();
    }

    public void createWallet(String address) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair kp = kpg.generateKeyPair();
        wallets.put(address, kp);
    }

    public PublicKey getPublicKey(String address) {
        return wallets.get(address).getPublic();
    }

    public PrivateKey getPrivateKey(String address) {
        return wallets.get(address).getPrivate();
    }
}
