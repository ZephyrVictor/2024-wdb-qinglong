package d;

import android.view.View;
import android.widget.AbsListView;
import androidx.appcompat.app.AlertController;

/* loaded from: classes.dex */
public final class c implements AbsListView.OnScrollListener {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ View f1961a;

    /* renamed from: b  reason: collision with root package name */
    public final /* synthetic */ View f1962b;

    public c(View view, View view2) {
        this.f1961a = view;
        this.f1962b = view2;
    }

    @Override // android.widget.AbsListView.OnScrollListener
    public final void onScroll(AbsListView absListView, int i2, int i3, int i4) {
        AlertController.b(absListView, this.f1961a, this.f1962b);
    }

    @Override // android.widget.AbsListView.OnScrollListener
    public final void onScrollStateChanged(AbsListView absListView, int i2) {
    }
}