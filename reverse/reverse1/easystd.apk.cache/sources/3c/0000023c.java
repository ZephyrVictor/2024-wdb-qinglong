package com.ctf.cma;

import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import androidx.fragment.app.h0;
import d.g;
import s1.e;
import v0.a;
import v0.b;

/* loaded from: classes.dex */
public class MainActivity extends g {

    /* renamed from: o  reason: collision with root package name */
    public h0 f1519o;

    @Override // androidx.fragment.app.p, androidx.activity.ComponentActivity, v.f, android.app.Activity
    public final void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        View inflate = getLayoutInflater().inflate(R.layout.activity_main, (ViewGroup) null, false);
        int i2 = R.id.btnSubmit;
        Button button = (Button) e.h(inflate, R.id.btnSubmit);
        if (button != null) {
            i2 = R.id.etInput;
            EditText editText = (EditText) e.h(inflate, R.id.etInput);
            if (editText != null) {
                LinearLayout linearLayout = (LinearLayout) inflate;
                this.f1519o = new h0(linearLayout, button, editText);
                setContentView(linearLayout);
                ((EditText) this.f1519o.c).setOnKeyListener(new a(this));
                ((Button) this.f1519o.f930b).setOnClickListener(new b(this));
                return;
            }
        }
        throw new NullPointerException("Missing required view with ID: ".concat(inflate.getResources().getResourceName(i2)));
    }
}