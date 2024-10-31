package d;

import android.view.View;
import androidx.appcompat.app.AlertController;

/* loaded from: classes.dex */
public final class d implements Runnable {

    /* renamed from: b  reason: collision with root package name */
    public final /* synthetic */ View f1963b;
    public final /* synthetic */ View c;

    /* renamed from: d  reason: collision with root package name */
    public final /* synthetic */ AlertController f1964d;

    public d(AlertController alertController, View view, View view2) {
        this.f1964d = alertController;
        this.f1963b = view;
        this.c = view2;
    }

    @Override // java.lang.Runnable
    public final void run() {
        AlertController.b(this.f1964d.f53f, this.f1963b, this.c);
    }
}