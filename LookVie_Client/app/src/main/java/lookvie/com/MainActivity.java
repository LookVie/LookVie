package lookvie.com;


import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    private Button searchButton;
    private EditText searchText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchButton = (Button)findViewById(R.id.searchButton);
        searchText = (EditText) findViewById(R.id.searchText);

        // mysql
        URLConnector url = new URLConnector("lookvies.c4gfbjjoxspj.us-east-2.rds.amazonaws.com");
        url.start();
        try {
            url.join();
        }
        catch(Exception e){
            e.printStackTrace();
        }

        String result = url.getTemp();
        System.out.println(ParseJSON(result));
        Toast.makeText(getApplicationContext(), "db: "+ParseJSON(result), Toast.LENGTH_LONG).show();

        ParseJSON(result);
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

    // JSON 데이터를 파싱합니다.
    // URLConnector로부터 받은 String이 JSON 문자열이기 때문입니다.
    public String ParseJSON(String target){
        try {
            JSONObject json = new JSONObject(target);
            JSONArray arr = json.getJSONArray("userdata");
            for(int i = 0; i < arr.length(); i++){
                JSONObject json2 = arr.getJSONObject(i);
                System.out.println(json2.getString("id"));
            }
            return "";
        }
        catch(Exception e){
            e.printStackTrace();
        }
        return null;
    }

}





