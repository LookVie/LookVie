package lookvie.com;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.support.annotation.NonNull;
import android.support.annotation.UiThread;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.naver.maps.geometry.LatLng;
import com.naver.maps.map.MapFragment;
import com.naver.maps.map.NaverMap;
import com.naver.maps.map.NaverMapSdk;
import com.naver.maps.map.OnMapReadyCallback;
import com.naver.maps.map.overlay.Marker;
import com.naver.maps.map.overlay.PathOverlay;
import com.odsay.odsayandroidsdk.API;
import com.odsay.odsayandroidsdk.ODsayData;
import com.odsay.odsayandroidsdk.ODsayService;
import com.odsay.odsayandroidsdk.OnResultCallbackListener;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.util.ArrayList;

public class MapActivity extends AppCompatActivity implements OnMapReadyCallback {
    private TextView textView;
    private String movieName;   // input movie text from main activity
    private EditText searchText;
    private Button searchButton;
    private Button theaterButton;
    Route route = new Route();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);
        /** Initialize variables */
        searchText = (EditText)findViewById(R.id.searchText);
        searchButton = (Button)findViewById(R.id.searchButton);
        theaterButton = (Button)findViewById(R.id.theaterButton);

        /** Show map */
        NaverMapSdk.getInstance(this).setClient(
                new NaverMapSdk.NaverCloudPlatformClient("jvtmsvggii"));

        MapFragment mapFragment = (MapFragment)getSupportFragmentManager().findFragmentById(R.id.map);
        if (mapFragment == null) {
            mapFragment = MapFragment.newInstance();
            getSupportFragmentManager().beginTransaction().add(R.id.map, mapFragment).commit();
        }

        mapFragment.getMapAsync( this);

        /** Get input text(movie) from main activity */
        Intent intent = getIntent();
        movieName = intent.getStringExtra("input"); // set movieName
        Toast.makeText(getApplicationContext(), "Input : " + movieName, Toast.LENGTH_LONG).show();
    }

    @UiThread
    @Override
    public void onMapReady(@NonNull NaverMap naverMap) {
        textView = (TextView) findViewById(R.id.textView);
        route.turnOnAPi(37.564108, 126.979413, 37.531460, 126.970966, getApplicationContext(), textView, naverMap);
    }

    /** Button Functions */
    public void onSearchClicked(View v)
    {
        String inputMovie = searchText.getText().toString();
        movieName = inputMovie;
        Toast.makeText(getApplicationContext(), "Search : " + movieName, Toast.LENGTH_LONG).show();
    }
    public void onTheatherClicked(View v)
    {
        Intent intent = new Intent(getApplicationContext(), TheaterActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        startActivity(intent);
    }
}
