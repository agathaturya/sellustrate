package com.sellustrate.sellustrate;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.TranslateAnimation;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button = findViewById(R.id.button2);
        button.setOnClickListener(this);

        Button buttonNew = findViewById(R.id.buttonNew);
        buttonNew.setOnClickListener(this);
    }

    public void onClick(View view)
    {
        doSomething(view);
    }

    public void doSomething(View view) {
        //The camera activity
        Intent cameraIntent = new Intent(this, CameraActivity.class);

        if (view.getId() == R.id.buttonNew)
            startActivity(cameraIntent);
        if (view.getId() == R.id.button2)
            slide();


    }

    //slides everything to the right
    public void slide()
    {
        ImageView signIn = findViewById(R.id.imageView7);
        TextView password = findViewById(R.id.password);
        TextView username = findViewById(R.id.username);
        Button buttonOld = findViewById(R.id.button2);
        Button buttonNew = findViewById(R.id.buttonNew);

        TranslateAnimation swipeRight = new TranslateAnimation(0.0f,850.0f,0.0f,0.0f);
        swipeRight.setDuration(600);
        swipeRight.setFillAfter(true);
        swipeRight.setFillEnabled(true);

        signIn.startAnimation(swipeRight);
        password.startAnimation(swipeRight);
        username.startAnimation(swipeRight);
        buttonOld.startAnimation(swipeRight);
        buttonNew.startAnimation(swipeRight);
        password.setEnabled(false);
        username.setEnabled(false);
    }

}
