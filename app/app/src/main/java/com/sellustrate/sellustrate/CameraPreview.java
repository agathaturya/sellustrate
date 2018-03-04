package com.sellustrate.sellustrate;

import android.content.Context;
import android.content.Intent;
import android.hardware.Camera;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.Button;


import java.io.IOException;



public class CameraPreview extends SurfaceView implements SurfaceHolder.Callback {
    private SurfaceHolder mSurfaceHolder;
    private Camera mCamera;

    // Constructor that obtains context and camera
    @SuppressWarnings("deprecation")
    public CameraPreview(Context context, Camera camera) {
        super(context);
        System.out.println("super was called in CameraPreview constructor");
        this.mCamera = camera;
        System.out.println("ehwehhddhfsheaz");
        this.mSurfaceHolder = this.getHolder();
        this.mSurfaceHolder.addCallback(this);
        this.mSurfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        System.out.println("end of camera constructor");

    }

    @Override
    public void surfaceCreated(SurfaceHolder surfaceHolder) {
    System.out.println(surfaceHolder.isCreating());
        try {
            mCamera.setPreviewDisplay(surfaceHolder);
            System.out.println();
            mCamera.startPreview();
            System.out.println("start preview in camPrev class is done");
        } catch (IOException e) {
            System.out.println("surfaceCreated failed:((((");
            // left blank for now
        }
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder surfaceHolder) {
        mCamera.stopPreview();
        mCamera.release();
    }

    @Override
    public void surfaceChanged(SurfaceHolder surfaceHolder, int format,
                               int width, int height) {
        mCamera.setDisplayOrientation(90);

        // start preview with new settings
        try {
            mCamera.setPreviewDisplay(surfaceHolder);
            mCamera.startPreview();
        } catch (Exception e) {
            // intentionally left blank for a test
        }
    }
}
