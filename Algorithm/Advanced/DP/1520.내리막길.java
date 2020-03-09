import java.util.*;

public class Main {
    public static int mod = 1000000;
    public static int[] dx = {0,0,1,-1};
    public static int[] dy = {1,-1,0,0};
    public static int go(int[][] a, int[][] d, int x, int y) {
        int n = a.length;
        int m = a[0].length;
        if (x == n-1 && y == m-1) {
            return 1;
        }
        if (d[x][y] >= 0) {
            return d[x][y];
        }
        d[x][y] = 0;
        for (int k=0; k<4; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (a[x][y] > a[nx][ny]) {
                    d[x][y] += go(a,d,nx,ny);
                }
            }
        }
        return d[x][y];
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][m];
        int[][] d = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                a[i][j] = sc.nextInt();
                d[i][j] = -1;
            }
        }
        System.out.println(go(a,d,0,0));
    }
}