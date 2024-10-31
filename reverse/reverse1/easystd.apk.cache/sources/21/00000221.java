package b;

import android.content.Intent;
import java.util.Collections;
import java.util.HashMap;

/* loaded from: classes.dex */
public final class b extends a {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ int f1461a;

    @Override // b.a
    public final Object a(int i2, Intent intent) {
        switch (this.f1461a) {
            case 0:
                if (i2 == -1 && intent != null) {
                    String[] stringArrayExtra = intent.getStringArrayExtra("androidx.activity.result.contract.extra.PERMISSIONS");
                    int[] intArrayExtra = intent.getIntArrayExtra("androidx.activity.result.contract.extra.PERMISSION_GRANT_RESULTS");
                    if (intArrayExtra != null && stringArrayExtra != null) {
                        HashMap hashMap = new HashMap();
                        int length = stringArrayExtra.length;
                        for (int i3 = 0; i3 < length; i3++) {
                            hashMap.put(stringArrayExtra[i3], Boolean.valueOf(intArrayExtra[i3] == 0));
                        }
                        return hashMap;
                    }
                }
                return Collections.emptyMap();
            default:
                return new androidx.activity.result.b(i2, intent);
        }
    }
}