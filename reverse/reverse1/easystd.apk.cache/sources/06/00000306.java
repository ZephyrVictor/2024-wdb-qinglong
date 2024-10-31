package d;

import android.os.Bundle;
import androidx.savedstate.a;
import java.util.Objects;

/* loaded from: classes.dex */
public final class e implements a.b {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ g f1965a;

    public e(g gVar) {
        this.f1965a = gVar;
    }

    @Override // androidx.savedstate.a.b
    public final Bundle a() {
        Bundle bundle = new Bundle();
        Objects.requireNonNull(this.f1965a.o());
        return bundle;
    }
}