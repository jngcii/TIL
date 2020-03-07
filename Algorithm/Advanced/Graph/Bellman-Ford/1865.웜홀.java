import java.util.*;
class Edge {
    int from, to, cost;
    Edge(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

}
public class Main {
    static final int inf = 100000000;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int w = sc.nextInt();
            Vector<Edge> a = new Vector<Edge>();
            for (int i=0; i<m; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int z = sc.nextInt();
                a.add(new Edge(x,y,z));
                a.add(new Edge(y,x,z));
            }
            for (int i=2*m; i<2*m+w; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int z = sc.nextInt();
                a.add(new Edge(x,y,-z));
            }
            int[] d = new int[n+1];
            for (int i=1; i<=n; i++) {
                d[i] = inf;
            }
            d[1] = 0;
            m = 2*m+w;
            boolean ok = false;
            for (int i=1; i<=n; i++) {
                for (Edge e : a) {
                    int x = e.from;
                    int y = e.to;
                    int z = e.cost;
                    if (d[x] != inf && d[y] > d[x]+z) {
                        d[y] = d[x]+z;
                        if (i == n) {
                            ok = true;
                        }
                    }
                }
            }
            if (ok) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}