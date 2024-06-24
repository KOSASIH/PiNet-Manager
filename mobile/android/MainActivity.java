package com.example.pinetmanager;

import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {
    private PiNetManagerApi api;

    @Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        api = PiNetManagerApi.getInstance();

        api.getNodes().enqueue(new Callback<List<Node>>() {
            @Override
            public void onResponse(Call<List<Node>> call, Response<List<Node>> response) {
                List<Node> nodes = response.body();
                Toast.makeText(MainActivity.this, "Nodes: " + nodes.size(), Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(Call<List<Node>> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
