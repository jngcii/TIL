import java.util.*;
public class Main {
    static final int inf = 100000000;
    private static int[] dijkstra(int n, int[][] a, int start) {
        int[] d = new int[n+1];
        boolean[]c = new boolean[n+1];
        for (int i=1; i<=n; i++) {
            d[i] = inf;
            c[i] = false;
        }
        d[start] = 0;
        for (int k=0; k<n-1; k++) {
            int min = inf+1;
            int x = -1;
            for (int i=1; i<=n; i++) {
                if (c[i] == false && min > d[i]) {
                    min = d[i];
                    x = i;
                }
            }
            c[x] = true;
            for (int i=1; i<=n; i++) {
                if (d[i] > d[x] + a[x][i]) {
                    d[i] = d[x] + a[x][i];
                }
            }
        }
        return d;
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][]a = new int[n+1][n+1];
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                a[i][j] = inf;
            }
        }
        int m = sc.nextInt();
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            if (a[x][y] > z) {
                a[x][y] = z;
            }
            if (a[y][x] > z) {
                a[y][x] = z;
            }
        }
        int v1 = sc.nextInt();
        int v2 = sc.nextInt();
        int[] dstart = dijkstra(n,a,1);
        int[] d1 = dijkstra(n,a,v1);
        int[] d2 = dijkstra(n,a,v2);
        int ans = dstart[v1] + d1[v2] + d2[n];
        int ans2 = dstart[v2] + d2[v1] + d1[n];
        if (ans > ans2) {
            ans = ans2;
        }
        if (ans >= inf) {
            ans = -1;
        }
        System.out.println(ans);
    }
}