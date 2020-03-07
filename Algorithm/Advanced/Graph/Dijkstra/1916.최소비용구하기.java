import java.util.*;
class Edge {
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}
public class Main {
    static final int inf = 1000000000;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Edge>[] a = (List<Edge>[]) new List[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<Edge>();
        }
        int m = sc.nextInt();
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            a[x].add(new Edge(y,z));
        }
        int start = sc.nextInt();
        int end = sc.nextInt();
        int[] d = new int[n+1];
        boolean[]c = new boolean[n+1];
        for (int i=1; i<=n; i++) {
            d[i] = inf;
            c[i] = false;
        }
        d[start] = 0;
        for (int k=0; k<n-1; k++) {
            m = inf+1;
            int x = -1;
            for (int i=1; i<=n; i++) {
                if (c[i] == false && m > d[i]) {
                    m = d[i];
                    x = i;
                }
            }
            c[x] = true;
            for (Edge y : a[x]) {
                if (d[y.to] > d[x] + y.cost) {
                    d[y.to] = d[x] + y.cost;
                }
            }
        }
        System.out.println(d[end]);
    }
}