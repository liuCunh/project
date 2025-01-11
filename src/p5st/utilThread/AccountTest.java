package p5st.utilThread;

public class AccountTest {
    public static void main(String[] args) {
        AccountThread accountThread = new AccountThread();
        new Thread(accountThread).start();
        new Thread(accountThread).start();
        new Thread(accountThread).start();
        new Thread(accountThread).start();

    }
}
class Account{
    private int balance = 10000;
    public void deposit(int amount){
        balance += amount;
    }
    public void withdraw(int amount){
        balance -= amount;
    }
    public int getBalance(){
        return balance;
    }
}
class AccountThread implements Runnable{
    Account account = new Account();
//    public AccountThread(Account account){
//        this.account = account;
//    }
//
    @Override
    public void run(){
        account.withdraw(100);
        System.out.println("线程"+Thread.currentThread().getName()+"--------------"+account.getBalance());
    }
}
