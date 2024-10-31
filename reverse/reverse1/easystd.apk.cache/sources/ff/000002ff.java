package d;

import android.content.Context;
import android.content.res.TypedArray;
import android.util.AttributeSet;
import android.view.ViewGroup;

/* loaded from: classes.dex */
public abstract class a {

    /* renamed from: d.a$a  reason: collision with other inner class name */
    /* loaded from: classes.dex */
    public static class C0023a extends ViewGroup.MarginLayoutParams {

        /* renamed from: a  reason: collision with root package name */
        public int f1958a;

        public C0023a() {
            super(-2, -2);
            this.f1958a = 8388627;
        }

        public C0023a(Context context, AttributeSet attributeSet) {
            super(context, attributeSet);
            this.f1958a = 0;
            TypedArray obtainStyledAttributes = context.obtainStyledAttributes(attributeSet, r.d.f2742b);
            this.f1958a = obtainStyledAttributes.getInt(0, 0);
            obtainStyledAttributes.recycle();
        }

        public C0023a(ViewGroup.LayoutParams layoutParams) {
            super(layoutParams);
            this.f1958a = 0;
        }

        public C0023a(C0023a c0023a) {
            super((ViewGroup.MarginLayoutParams) c0023a);
            this.f1958a = 0;
            this.f1958a = c0023a.f1958a;
        }
    }

    /* loaded from: classes.dex */
    public interface b {
        void a();
    }

    @Deprecated
    /* loaded from: classes.dex */
    public static abstract class c {
        public abstract void a();
    }
}