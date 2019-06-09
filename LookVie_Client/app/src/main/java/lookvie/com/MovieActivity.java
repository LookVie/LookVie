package lookvie.com;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;

import java.util.ArrayList;

public class MovieActivity extends AppCompatActivity {
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.movie_info);

        TextView textView = (TextView) findViewById(R.id.textView2);
        Intent intent = getIntent();
        int index = intent.getIntExtra("index",0);
        ArrayList<String> ReceiveArr = intent.getStringArrayListExtra("ArrayList"); //어레이 리스트 받아옴

        textView.setText(ReceiveArr.get(index));
    }

    public void onTheatherClicked(View v)
    {
        Intent intent = new Intent(getApplicationContext(), TheaterActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        startActivity(intent);
    }
}
