package lookvie.com;


import android.content.ContentValues;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class MainActivity extends AppCompatActivity {
    private Button searchButton;
    private EditText searchText;
    private URL url;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchButton = (Button)findViewById(R.id.searchButton);
        searchText = (EditText) findViewById(R.id.searchText);

        // URL 설정.
        String url = "http://52.53.228.72/auth/ict_timetable";

        // AsyncTask를 통해 HttpURLConnection 수행.
        NetworkTask networkTask = new NetworkTask(url, null);
        networkTask.execute();

    }

    public void onSearchClicked(View v)
    {
        //Toast.makeText(getApplicationContext(), "It has been clicked!", Toast.LENGTH_LONG).show();
        String inputMovie = searchText.getText().toString();

        Intent intent = new Intent(getApplicationContext(), MapActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        intent.putExtra("input", inputMovie);
        startActivity(intent);
    }

    public class NetworkTask extends AsyncTask<Void, Void, String> {

        private String url;
        private ContentValues values;

        public NetworkTask(String url, ContentValues values) {

            this.url = url;
            this.values = values;
        }

        @Override
        protected String doInBackground(Void... params) {

            String result; // 요청 결과를 저장할 변수.
            RequestHttpURLConnection requestHttpURLConnection = new RequestHttpURLConnection();
            result = requestHttpURLConnection.request(url, values); // 해당 URL로 부터 결과물을 얻어온다.

            return result;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            //doInBackground()로 부터 리턴된 값이 onPostExecute()의 매개변수로 넘어오므로 s를 출력한다.
            JSONObject jsonObject;
            try {
                jsonObject = new JSONObject(s); //result를 인자로 넣어 jsonObject를 생성한다.
                //System.out.println(jsonObject);
            } catch(JSONException e) {
                e.printStackTrace();
            }
            //Toast.makeText(getApplicationContext(), "output"+s, Toast.LENGTH_LONG).show();
            //tv_outPut.setText(s);
        }
    }
}





