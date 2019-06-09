package lookvie.com;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

public class TheaterActivity extends AppCompatActivity {

    private String movieName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_theater);

        Intent intent = getIntent();
        movieName = intent.getStringExtra("input");
        //Toast.makeText(getApplicationContext(), "Input : " + movieName, Toast.LENGTH_LONG).show();
    }
}
