package lookvie.com;


import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    private Button searchButton;
    private EditText searchText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchButton = (Button)findViewById(R.id.searchButton);
        searchText = (EditText) findViewById(R.id.searchText);

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


}





