/*package lookvie.com;

import android.content.Context;
import android.graphics.Color;
import android.util.Log;
import android.widget.TextView;

import com.naver.maps.geometry.LatLng;
import com.naver.maps.map.NaverMap;
import com.naver.maps.map.overlay.Marker;
import com.naver.maps.map.overlay.OverlayImage;
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
import java.util.Arrays;

public class RouteTest {

    private JSONObject jsonObject = new JSONObject();

    public void routeText(Double sLat, Double sLng, Double eLat, Double eLng, final Context context) {
        ODsayService odsayService = ODsayService.init(context, "jS8GHAna7ORlgTBz3ccOT/b48MertkNiGzXI2jkjNpM");
        odsayService.setReadTimeout(5000);
        odsayService.setConnectionTimeout(5000);
        odsayService.requestSearchPubTransPath(Double.toString(sLng), Double.toString(sLat), Double.toString(eLng),
                Double.toString(eLat), "0", "0", "0", new OnResultCallbackListener() {
                    @Override
                    public void onSuccess(ODsayData odsayData, API api) {
                        jsonObject = odsayData.getJson();

                    }

                    @Override
                    public void onError(int i, String errorMessage, API api) {
                        Log.i("SearchAPi", errorMessage);
                    }
                });

    }

    // 이동방법 파싱
    private String parseRoute(JSONObject jsonObject, Context context) {
        String routedetail = "";
        try {
            JSONObject result = jsonObject.getJSONObject("result");
            JSONArray pathArray = result.getJSONArray("path");
// pathArray 안의 경로 갯수
            int pathArraycount = pathArray.length();
            for (int i = 0; i < pathArraycount; i++) {
                JSONObject pathArrayDetailOBJ = pathArray.getJSONObject(i);
                //int pathType = pathArrayDetailOBJ.getInt("pathType");
                JSONObject infoOBJ = pathArrayDetailOBJ.getJSONObject("info");
                int payment = infoOBJ.getInt("payment"); // 요금
                //int totalWalk = infoOBJ.getInt("totalWalk");
                int totalTime = infoOBJ.getInt("totalTime"); // 소요시간
                String mapObj = infoOBJ.getString("mapObj"); // 경로 디테일 조회 아이디
                //String firstStartStation = infoOBJ.getString("firstStartStation");
                //String lastEndStation = infoOBJ.getString("lastEndStation");
                JSONArray subPathArray = pathArrayDetailOBJ.getJSONArray("subPath");
                int subPathArraycount = subPathArray.length();
                int busID = 0;
                for (int j = 0; j < subPathArraycount; j++) {
                    JSONObject subPathOBJ = subPathArray.getJSONObject(j);
                    int Type = subPathOBJ.getInt("trafficType"); // 이동방법
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
                            routedetail += startName + "에서 승차 후 ";
                            routedetail += endName + "에서 하차";
                        }


                    }
                    int distance = subPathOBJ.getInt("distance"); // 이동길이
                    routedetail += "\n( " + Integer.toString(distance) + "m 이동. ";
                    int sectionTime = subPathOBJ.getInt("sectionTime"); // 이동시간
                    routedetail += Integer.toString(sectionTime) + "분 소요 )\n";
                    totalTime += sectionTime;
                }
                routedetail += Integer.toString(payment) + "원\n" + "총" + Integer.toString(totalTime) + "분 소요\n\n ";
                break;
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return routedetail;
    }

    private void turnOnAPI2(String mapObj, Context context, final NaverMap naverMap) {
        ODsayService odsayService;
        odsayService = ODsayService.init(context, "jS8GHAna7ORlgTBz3ccOT/b48MertkNiGzXI2jkjNpM");
        odsayService.setReadTimeout(5000);
        odsayService.setConnectionTimeout(5000);
        odsayService.requestLoadLane("0:0@" + mapObj, new OnResultCallbackListener() {
            @Override
            public void onSuccess(ODsayData oDsayData, API api) {
                jsonObject = oDsayData.getJson();
                drawOnMap(jsonObject, naverMap);
            }

            @Override
            public void onError(int i, String errorMessage, API api) {
                Log.i("SearchAPi", errorMessage);
            }
        });
    }

    // 경로 파싱
    private void drawOnMap(JSONObject jsonObject, NaverMap naverMap) {
        PathOverlay path = new PathOverlay();
        ArrayList<LatLng> latLngArray = new ArrayList<>();
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
            }
            path.setCoords(latLngArray);
            path.setColor(Color.GREEN);
            path.setMap(naverMap);

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }


}*/


