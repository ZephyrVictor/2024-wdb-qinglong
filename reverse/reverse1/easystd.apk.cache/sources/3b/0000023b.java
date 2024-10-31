package com.ctf.cma;

/* loaded from: classes.dex */
public class Check {
    static {
        System.loadLibrary("cma");
    }

    public static native boolean validate(String str);
}