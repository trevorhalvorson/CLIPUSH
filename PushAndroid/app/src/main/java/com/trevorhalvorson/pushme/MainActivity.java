package com.trevorhalvorson.pushme;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;

import java.net.URL;

import me.pushy.sdk.Pushy;

/**
 * Basic Pushy.me registration app created from https://pushy.me/docs/android
 * Also see: https://github.com/pushy-me/pushy-demo-android
 */
public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Pushy.listen(this);
        registerForPushy();
    }

    private void registerForPushy() {
        new RegisterForPushNotificationsAsync().execute();
    }

    private class RegisterForPushNotificationsAsync extends AsyncTask<Void, Void, String> {
        protected String doInBackground(Void... params) {
            String deviceToken = null;
            try {
                // Assign a unique token to this device
                deviceToken = Pushy.register(getApplicationContext());

                // Log it for debugging purposes
                Log.d(TAG, "Pushy device token: " + deviceToken);

                // TODO: Send the token to your backend server via an HTTP GET request
                new URL("https://{YOUR_API_HOSTNAME}/register/device?token=" + deviceToken).openConnection();
            }
            catch (Exception exc) {
                Log.e(TAG, "doInBackground: ", exc);
            }

            // Success
            return deviceToken;
        }

        @Override
        protected void onPostExecute(String deviceToken) {
            TextView deviceIdText = (TextView) findViewById(R.id.deviceIdText);
            deviceIdText.setText(deviceToken);
        }
    }
}
