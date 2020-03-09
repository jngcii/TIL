// Bottom up

import java.util.*;

class Element implements Comparable<Element> {
    int row, col, val;
    Element(int row, int col, int val) {
        this.row = row;
        this.col = col;
        this.val = val;
    }
    public int compareTo(Element that) {
        if (this.val > that.val) return -1;
        else if (this.val < that.val) return 1;
        else return 0;
    }
}
public class Main {
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n][n];
        Element[] b = new Element[n*n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                a[i][j] = sc.nextInt();
                b[i*n+j] = new Element(i,j,a[i][j]);
            }
        }
        Arrays.sort(b,0,n*n);
        int[][] d = new int[n][n];
        for (int i=0; i<n*n; i++) {
            int x = b[i].row;
            int y = b[i].col;
            d[x][y] = 1;
            // (x, y) -> (nx, ny)
            for (int k=0; k<4; k++) {
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (a[x][y] < a[nx][ny]) {
                    d[x][y] = Math.max(d[x][y],d[nx][ny]+1);
                }
            }
        }
        int ans = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (ans < d[i][j]) {
                    ans = d[i][j];
                }
            }
        }
        System.out.println(ans);
    }
}

// Top down
import java.util.*;
public class Main {
    static int n;
    static int[][] a = new int[500][500];
    static int[][] d = new int[500][500];
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0};
    static int go(int i, int j) {
        if (d[i][j] != 0) {
            return d[i][j];
        }
        d[i][j] = 1;
        for (int k=0; k<4; k++) {
            int x = i+dx[k];
            int y = j+dy[k];
            if (x < 0 || x >= n || y < 0 || y >= n) continue;
            if (a[i][j] < a[x][y]) {
                d[i][j] = Math.max(d[i][j], go(x, y) + 1);
            }
        }
        return d[i][j];
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        int ans = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                ans = Math.max(ans, go(i, j));
            }
        }
        System.out.println(ans);
    }
}