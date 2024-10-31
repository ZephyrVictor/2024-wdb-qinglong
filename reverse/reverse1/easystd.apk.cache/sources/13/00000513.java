package z0;

import android.view.View;
import com.google.android.material.behavior.SwipeDismissBehavior;
import f0.p;
import f0.s;
import g0.d;
import java.util.Objects;
import java.util.WeakHashMap;

/* loaded from: classes.dex */
public final class a implements d {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ SwipeDismissBehavior f3204a;

    public a(SwipeDismissBehavior swipeDismissBehavior) {
        this.f3204a = swipeDismissBehavior;
    }

    @Override // g0.d
    public final boolean a(View view) {
        boolean z2 = false;
        if (this.f3204a.s(view)) {
            WeakHashMap<View, s> weakHashMap = p.f2169a;
            boolean z3 = view.getLayoutDirection() == 1;
            int i2 = this.f3204a.c;
            if ((i2 == 0 && z3) || (i2 == 1 && !z3)) {
                z2 = true;
            }
            int width = view.getWidth();
            if (z2) {
                width = -width;
            }
            p.q(view, width);
            view.setAlpha(0.0f);
            Objects.requireNonNull(this.f3204a);
            return true;
        }
        return false;
    }
}