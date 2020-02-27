import java.util.*;
public class Main {
    static int[][] a;
    static int[][] next;
    static final int inf = 1000000000;
    static void path(int x, int y) {
        if (next[x][y] == -1) {
            System.out.println(0);
            return;
        }
        Queue<Integer> q = new LinkedList<>();
        q.add(x);
        while (x != y) {
            x = next[x][y];
            q.add(x);
        }
        System.out.print(q.size() + " ");
        while (!q.isEmpty()) {
            System.out.print(q.remove() + " ");
        }
        System.out.println();
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        a = new int[n+1][n+1];
        next = new int[n+1][n+1];
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (i == j) {
                    a[i][j] = 0;
                } else {
                    a[i][j] = inf;
                }
                next[i][j] = -1;
            }
        }
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            if (a[x][y] == 0) {
                a[x][y] = z;
            } else {
                a[x][y] = Math.min(a[x][y],z);
                next[x][y] = y;
            }
        }
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    if (a[i][j] > a[i][k] + a[k][j]) {
                        a[i][j] = a[i][k] + a[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (a[i][j] == inf) {
                    System.out.print("0 ");
                } else {
                    System.out.print(a[i][j] + " ");
                }
            }
            System.out.println();
        }
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (i == j) {
                    System.out.println(0);
                } else if (a[i][j] == inf) {
                    System.out.println(0);
                } else {
                    path(i, j);
                }
            }
        }
    }
}