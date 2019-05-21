package lookvie.com;

import android.content.Context;
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
import android.view.ViewGroup;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.naver.maps.geometry.LatLng;
import com.naver.maps.map.MapFragment;
import com.naver.maps.map.NaverMap;
import com.naver.maps.map.NaverMapSdk;
import com.naver.maps.map.OnMapReadyCallback;
import com.naver.maps.map.overlay.InfoWindow;
import com.naver.maps.map.overlay.LocationOverlay;
import com.naver.maps.map.overlay.Marker;
import com.naver.maps.map.overlay.Overlay;
import com.naver.maps.map.overlay.PathOverlay;
import com.odsay.odsayandroidsdk.API;
import com.odsay.odsayandroidsdk.ODsayData;
import com.odsay.odsayandroidsdk.ODsayService;
import com.odsay.odsayandroidsdk.OnResultCallbackListener;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class MapActivity extends AppCompatActivity implements OnMapReadyCallback {

    private JSONObject jsonObject = new JSONObject();
    private ArrayList<Marker> markerList = new ArrayList<>();
    private ArrayList<InfoWindow> InfoWindow = new ArrayList<>();
    private ArrayList<LatLng> finalList = new ArrayList<>();
    private ArrayList<LatLng> finalfinalList = new ArrayList<>();
    private ArrayList<String> finalrouteList = new ArrayList<>();
    private ArrayList<String> finalListName = new ArrayList<>();
    private ArrayList<InfoWindow> finalInfowindow = new ArrayList<>();
    private HashMap<LatLng,Integer> desList = new HashMap<>();
    private HashMap<LatLng,String> routeList = new HashMap<>();
    private HashMap<LatLng,String> mapO = new HashMap<>();
    private ListView listView;

    int count=0;
    int sizecount=0;
    int finalindex=0;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listView =(ListView)findViewById(R.id.listView);
        NaverMapSdk.getInstance(this).setClient(
                new NaverMapSdk.NaverCloudPlatformClient("jvtmsvggii"));

        MapFragment mapFragment = (MapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        if (mapFragment == null) {
            mapFragment = MapFragment.newInstance();
            getSupportFragmentManager().beginTransaction().add(R.id.map, mapFragment).commit();
        }

        mapFragment.getMapAsync(this); //NaverMap 띄움

    }

    @UiThread
    @Override
    public void onMapReady(@NonNull NaverMap naverMap) {
        ArrayList<LatLng> latlngss = new ArrayList<>(); // 영화관 좌표 리스트 담을 배열
        ArrayList<LatLng> sortedTheater1 = new ArrayList<>(); // 거리순으로 정렬된 영화관들
        LatLng starting = new LatLng(37.564108, 126.979413);

        latlngss.add(new LatLng(37.563807,126.979313));
        latlngss.add(new LatLng(37.531460, 126.975966));
        latlngss.add(new LatLng(37.521460, 126.970966));
        latlngss.add(new LatLng(37.511460, 126.960966));
        latlngss.add(new LatLng(37.501460, 126.965966));
        latlngss.add(new LatLng(37.491460, 126.985966));
        latlngss.add(new LatLng(37.541460, 126.980966));
        latlngss.add(new LatLng(37.551460, 126.960966));
        latlngss.add(new LatLng(37.561460, 126.950966));
        latlngss.add(new LatLng(37.521460, 126.940966));
        latlngss.add(new LatLng(37.561360, 126.930966));
        latlngss.add(new LatLng(37.491460, 126.920966));
        latlngss.add(new LatLng(37.481460, 126.910966));
        latlngss.add(new LatLng(37.471460, 126.900966));
        latlngss.add(new LatLng(37.461460, 126.890966));
        latlngss.add(new LatLng(37.471460, 126.890966));
        latlngss.add(new LatLng(37.481460, 126.890966));
        latlngss.add(new LatLng(37.491460, 126.870966));
        latlngss.add(new LatLng(37.451460, 126.830096));
        latlngss.add(new LatLng(37.441460, 126.820966));
        latlngss.add(new LatLng(37.431460, 126.830966));
        latlngss.add(new LatLng(37.421460, 126.810966));
        latlngss.add(new LatLng(37.411460, 126.830966));
        latlngss.add(new LatLng(37.501460, 126.820966));
        latlngss.add(new LatLng(37.421460, 126.850966));
        latlngss.add(new LatLng(37.461460, 126.830966));
        latlngss.add(new LatLng(37.461460, 126.840966));
        latlngss.add(new LatLng(37.461460, 126.850966));
        latlngss.add(new LatLng(37.521460, 126.820966));
        latlngss.add(new LatLng(37.531460, 126.830966));
        latlngss.add(new LatLng(37.591460, 126.810966));
        latlngss.add(new LatLng(37.581460, 126.850966));
        latlngss.add(new LatLng(37.531460, 126.970966));
        latlngss.add(new LatLng(37.571460, 126.980966));
        latlngss.add(new LatLng(37.541460, 126.990966));
        latlngss.add(new LatLng(37.551460, 126.990966));
        latlngss.add(new LatLng(37.561460, 126.990966));
        latlngss.add(new LatLng(37.561460, 126.990966)); // 테스트용으로 임시 추가

        sortTheater(starting,latlngss,naverMap);
    }

    public void turnOnAPI(final LatLng startingPoint, final LatLng destination, final NaverMap naverMap) {
        ODsayService odsayService = ODsayService.init(getApplicationContext(), "jS8GHAna7ORlgTBz3ccOT/b48MertkNiGzXI2jkjNpM");
        odsayService.setReadTimeout(5000);
        odsayService.setConnectionTimeout(5000);
        odsayService.requestSearchPubTransPath(Double.toString(startingPoint.longitude), Double.toString(startingPoint.latitude),
                Double.toString(destination.longitude), Double.toString(destination.latitude), "0", "0", "0", new OnResultCallbackListener() {
                    @Override
                    public void onSuccess(ODsayData odsayData, API api) {
                        jsonObject = odsayData.getJson();
                        parseRoute(jsonObject, startingPoint,destination, naverMap);
                    }

                    @Override
                    public void onError(int i, String errorMessage, API api) {
                        Log.i("SearchAPi", errorMessage);
                    }
                });

    }

    // 이동방법 파싱
    private void parseRoute(JSONObject jsonObject, LatLng startingPoint, LatLng destination, NaverMap naverMap) {
        String routedetail = "";
        try {
            JSONObject result = jsonObject.getJSONObject("result");
            JSONArray pathArray = result.getJSONArray("path");
            JSONObject pathArrayDetailOBJ = pathArray.getJSONObject(0);
            JSONObject infoOBJ = pathArrayDetailOBJ.getJSONObject("info");
            int payment = infoOBJ.getInt("payment");
            int totalTime = infoOBJ.getInt("totalTime");
            String mapObj = infoOBJ.getString("mapObj"); // 맵에 경로 그리기 위한 String
            JSONArray subPathArray = pathArrayDetailOBJ.getJSONArray("subPath");
            int subPathArraycount = subPathArray.length();
            int busID = 0;
            for (int j = 0; j < subPathArraycount; j++) {
                JSONObject subPathOBJ = subPathArray.getJSONObject(j);
                int Type = subPathOBJ.getInt("trafficType");
                switch (Type) {
                    case 1:
                        routedetail += "지하철 ";
                        break;
                    case 2:
                        routedetail += "버스 ";
                        break;
                    default:
                        routedetail += "도보 ";
                        break;
                }
                if (Type == 1 || Type == 2) {
                    String startName = subPathOBJ.getString("startName"); // 출발지
                    String endName = subPathOBJ.getString("endName"); // 도착지
                    JSONArray laneObj = subPathOBJ.getJSONArray("lane");

                    if (Type == 1) { // 지하철
                        String subwayName = laneObj.getJSONObject(0).getString("name"); // 지하철 호선
                        routedetail += subwayName + " ";
                        routedetail += startName + "역 에서 승차 후 ";
                        routedetail += endName + "역 에서 하차";
                    }
                    if (Type == 2) { // 버스..
                        String busNo = laneObj.getJSONObject(0).getString("busNo"); // 버스번호
                        String busroute = " [" + busNo + "] 번 버스 ";
                        routedetail += busroute;
                        routedetail += startName + " 에서 승차 후 ";
                        routedetail += endName + " 에서 하차";
                    }
                }

                int distance = subPathOBJ.getInt("distance"); // 이동길이
                routedetail += "\n( " + Integer.toString(distance) + "m 이동. ";
                int sectionTime = subPathOBJ.getInt("sectionTime"); // 이동시간
                routedetail += Integer.toString(sectionTime) + "분 소요 )\n";
            }
            routedetail += Integer.toString(payment) + "원\n" + "총" + Integer.toString(totalTime) + "분 소요\n\n ";
            desList.put(destination,totalTime);
            mapO.put(destination,mapObj);
            routeList.put(destination,routedetail);
            count++;
            if(count==sizecount) {
                finalList = sortByTime();
                while(finalfinalList.size()<3 && finalindex<finalList.size()) {
                        int setcolor = finalfinalList.size();
                        turnOnAPI2(mapO.get(finalList.get(finalindex)), startingPoint, finalList.get(finalindex), naverMap,setcolor++);
                        finalfinalList.add(finalList.get(finalindex));
                        finalrouteList.add(routeList.get(finalList.get(finalindex)));
                        Log.d("sorted", routeList.get(finalList.get(finalindex)));
                        finalindex++;
                    }

                for(int i=0;i<finalfinalList.size();i++){
                    finalListName.add("영화관 "+ (i+1));
                }
                ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, finalListName){
                    @Override

                    public View getView(int position, View convertView, ViewGroup parent) {
                        View view = super.getView(position, convertView, parent);
                        TextView tv = (TextView) view.findViewById(android.R.id.text1);
                        if(position == 0) {
                            tv.setTextColor(Color.GREEN);
                        }
                        else if (position == 1){
                            tv.setTextColor(Color.BLUE);
                        }
                        else{
                            tv.setTextColor(Color.MAGENTA);
                        }
                        return view;
                    }
                };
                listView.setAdapter(adapter) ;
                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Intent intent = new Intent(getApplicationContext(),MovieActivity.class);
                        intent.putExtra("index", position);
                        intent.putStringArrayListExtra("ArrayList", finalrouteList);
                        startActivity(intent);
                    }
                });
            }

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private void turnOnAPI2(String mapObj, final LatLng startingPoint, final LatLng destination, final NaverMap naverMap,final int index) {
        ODsayService odsayService;
        odsayService = ODsayService.init(getApplicationContext(), "jS8GHAna7ORlgTBz3ccOT/b48MertkNiGzXI2jkjNpM");
        odsayService.setReadTimeout(5000);
        odsayService.setConnectionTimeout(5000);
        odsayService.requestLoadLane("0:0@" + mapObj, new OnResultCallbackListener() {
            @Override
            public void onSuccess(ODsayData oDsayData, API api) {
                jsonObject = oDsayData.getJson();
                drawOnMap(jsonObject, startingPoint, destination, naverMap,index);
            }

            @Override
            public void onError(int i, String errorMessage, API api) {
                Log.i("SearchAPi", errorMessage);
            }
        });
    }

    // 경로 파싱
    private void drawOnMap(JSONObject jsonObject, LatLng startingPoint, LatLng destination, NaverMap naverMap,int index) {
        PathOverlay path = new PathOverlay();
        PathOverlay sPath = new PathOverlay();
        PathOverlay ePath = new PathOverlay();
        ArrayList<LatLng> latLngArray = new ArrayList<>();
        ArrayList<LatLng> seLatLngArray = new ArrayList<>();
        Marker marker = new Marker();

        try {
            JSONObject result = jsonObject.getJSONObject("result");
            JSONArray laneArray = result.getJSONArray("lane");
            JSONArray sectionArray = laneArray.getJSONObject(0).getJSONArray("section");
            JSONArray graphPosArray = sectionArray.getJSONObject(0).getJSONArray("graphPos");
            int graphPosCount = graphPosArray.length();

            for (int i = 0; i < graphPosCount; i++) {
                Double lat = graphPosArray.getJSONObject(i).getDouble("y");
                Double lng = graphPosArray.getJSONObject(i).getDouble("x");
                latLngArray.add(new LatLng(lat, lng));
                if (i == 0) {
                    seLatLngArray.add(startingPoint);
                    seLatLngArray.add(new LatLng(lat, lng));
                    sPath.setCoords(seLatLngArray);
                    seLatLngArray.clear();
                }
                if (i == graphPosCount - 1) {
                    seLatLngArray.add(new LatLng(lat, lng));
                    seLatLngArray.add(destination);
                    ePath.setCoords(seLatLngArray);
                }
            }
            path.setCoords(latLngArray);
            marker.setPosition(destination);
            if(index==0) {
                path.setColor(Color.GREEN);
                sPath.setColor(Color.GREEN);
                ePath.setColor(Color.GREEN);
                marker.setIconTintColor(Color.GREEN);
            }
            if(index==1) {
                path.setColor(Color.BLUE);
                sPath.setColor(Color.BLUE);
                ePath.setColor(Color.BLUE);
                marker.setIconTintColor(Color.BLUE);
            }
            if(index==2) {
                path.setColor(Color.MAGENTA);
                sPath.setColor(Color.MAGENTA);
                ePath.setColor(Color.MAGENTA);
                marker.setIconTintColor(Color.MAGENTA);
            }
            path.setMap(naverMap);
            sPath.setMap(naverMap);
            ePath.setMap(naverMap);
            markerList.add(marker);
            marker.setMap(naverMap);
            clickedMarker();
            Log.d("marker",Integer.toString(markerList.size()));
            Log.d("marker",Integer.toString(finalInfowindow.size()));

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private ArrayList<LatLng> sortByDistanceH(LatLng startingPoint, ArrayList<LatLng> theaters){
        //HashMap 이용한 sort (느림)

        ArrayList<LatLng> sortedByDistance = new ArrayList<LatLng>();
        HashMap<Double,LatLng> distanceList = new HashMap<>();

        for (int i = 0; i < theaters.size(); i++) {
            distanceList.put(startingPoint.distanceTo(theaters.get(i)),theaters.get(i));
        }
        TreeMap<Double,LatLng> tm = new TreeMap<>(distanceList);
        Set<Double> keyset = distanceList.keySet();
        Iterator<Double> keyiterator = tm.keySet( ).iterator( );

        while(keyiterator.hasNext()) {
            Double key = keyiterator.next();
            sortedByDistance.add(tm.get(key));
        }
        for (int i = 0; i < sortedByDistance.size(); i++) {
            Log.d("bb", sortedByDistance.get(i).toString());
        }
        return sortedByDistance;
    }

    private ArrayList<LatLng> sortByDistance(LatLng startingPoint, ArrayList<LatLng> theaters,NaverMap naverMap) {
        // 2차원배열 sort (좀더빠름)
        ArrayList<LatLng> sortedByDistance = new ArrayList<LatLng>();
        double[][] distanceList = new double[50][2];
        Log.d("bb", Integer.toString(theaters.size()));
        for (int i = 0; i < theaters.size(); i++) {
            distanceList[i][0] = i;
            distanceList[i][1] = startingPoint.distanceTo(theaters.get(i));
        }
        java.util.Arrays.sort(distanceList, 0, theaters.size(), new java.util.Comparator<double[]>() {
            public int compare(double[] a, double[] b) {
                return Double.compare(a[1], b[1]);
            }
        });
        if (theaters.size() >= 6) {
            for (int i = 0; i < 6; i++) {
                if(distanceList[i][1]<=700) {
                    finalfinalList.add(theaters.get((int) distanceList[i][0]));
                    finalrouteList.add("700m 이내 도보로 이동");
                    shortDistance(startingPoint,theaters.get((int)distanceList[i][0]),naverMap,finalfinalList.size()-1);
                }
                else {
                    sortedByDistance.add(theaters.get((int) distanceList[i][0]));
                }
            }
        } else {
            for (int i = 0; i < theaters.size(); i++) {
                if(distanceList[i][1]<=700) {
                    finalfinalList.add(theaters.get((int) distanceList[i][0]));
                    finalrouteList.add("700m 이내 도보로 이동");
                    shortDistance(startingPoint,theaters.get((int)distanceList[i][0]),naverMap,finalfinalList.size()-1);
                }
                else {
                    sortedByDistance.add(theaters.get((int) distanceList[i][0]));
                }
            }
        }
        return sortedByDistance;
    }

    private ArrayList<LatLng> sortByTime() { // 소요시간으로 정렬
        ArrayList<LatLng> sortedByTime = new ArrayList<LatLng>();
        Iterator keyiterator = sortByValue(desList).iterator();
        while(keyiterator.hasNext()) {
            sortedByTime.add((LatLng)keyiterator.next());
        }
        for (int i = 0; i < sortedByTime.size(); i++) {
            Log.d("time", Integer.toString(desList.get(sortedByTime.get(i))));
        }
        return sortedByTime;
    }

    private ArrayList<LatLng> sortByValue(final HashMap<LatLng,Integer> map){
        ArrayList<LatLng> keySetList = new ArrayList<>(map.keySet());
        Collections.sort(keySetList, new Comparator<LatLng>() {
            @Override
            public int compare(LatLng o1, LatLng o2) {
                return map.get(o1).compareTo(map.get(o2));
            }
        });
        return keySetList;
    }

    private void clickedMarker(){

        final Marker marker = markerList.get(markerList.size()-1);
        final InfoWindow infoWindow = new InfoWindow();
        infoWindow.setAdapter(new InfoWindow.DefaultTextAdapter(getApplicationContext()) {
            @NonNull
            @Override
            public CharSequence getText(@NonNull InfoWindow infoWindow) {
                return "영화관 " + markerList.size();
            }
        });

        Marker.OnClickListener listener = new Marker.OnClickListener() {
            @Override
            public boolean onClick(@NonNull Overlay overlay) {
                if (marker.getInfoWindow() == null) {
                    infoWindow.open(marker);
                } else {
                    infoWindow.close();
                }

                return true;
            }
        };
        marker.setOnClickListener(listener);
        finalInfowindow.add(infoWindow);
    }

    private void sortTheater(LatLng starting,ArrayList<LatLng> latlngss,NaverMap naverMap){
        if(latlngss.size()==1){
            Toast.makeText(getApplicationContext(),"영화를 상영하는 영화관이 없습니다",Toast.LENGTH_LONG).show();
        }
        else {
            ArrayList<LatLng> sortedTheater1 = sortByDistance(starting, latlngss, naverMap); // 거리로 먼저 영화관 추려낸 뒤 (바로 소요시간으로 추려낼 시 타임아웃 문제)
            sizecount = sortedTheater1.size();
            for (int i = 0; i < sizecount; i++) {
                turnOnAPI(starting, sortedTheater1.get(i), naverMap);
                // 거리로 추려낸 영화관들을 소요시간으로 다시 추려낸 후, listview에 경로 String 올리고, Map에 경로 그림.
            }
        }
    }

    private void shortDistance(LatLng starting,LatLng destination,NaverMap naverMap,int index){
        Marker marker = new Marker();
        PathOverlay path = new PathOverlay();
        ArrayList<LatLng> se = new ArrayList<>();
        se.add(starting);
        se.add(destination);
        path.setCoords(se);
        marker.setPosition(destination);
        if(index==0) {
            path.setColor(Color.GREEN);
            marker.setIconTintColor(Color.GREEN);
        }
        if(index==1) {
            path.setColor(Color.BLUE);
            marker.setIconTintColor(Color.BLUE);
        }
        if(index==2) {
            path.setColor(Color.MAGENTA);
            marker.setIconTintColor(Color.MAGENTA);
        }
        path.setMap(naverMap);
        marker.setMap(naverMap);
        markerList.add(marker);
        clickedMarker();
    }
}






