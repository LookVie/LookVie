import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;


public class Client {
    
    private Socket mSocket;

    private BufferedReader mIn;
    private PrintWriter mOut;
    static Scanner input = new Scanner(System.in);
    static String sendData;
    public Client(String ip, int port) {
        try {
            // 서버에 요청 보내기
            System.out.println(" 연결대기중 ");
            mSocket = new Socket(ip, port);
            System.out.println(ip + " 연결됨");

            mIn = new BufferedReader(
                    new InputStreamReader(mSocket.getInputStream()));
            mOut = new PrintWriter(mSocket.getOutputStream());

            // 메세지 전달
            while(true){
                System.out.println(mIn.readLine());

                System.out.print(">>>");
                sendData = input.nextLine();
                
                mOut.write(sendData);
                mOut.flush();
            }

            // 응답 출력


        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            // 소켓 닫기
            try {
                mSocket.close();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    public static void main(String[] args) {

        String ip = "127.0.0.1";
        int port = 5000;
        System.out.println("waiting");

        new Client(ip, port);
    }
}