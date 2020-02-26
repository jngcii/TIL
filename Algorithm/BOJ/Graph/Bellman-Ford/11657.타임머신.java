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
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<Edge> a = new ArrayList<Edge>();
        for (int i=0; i<m; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            int cost = sc.nextInt();
            a.add(new Edge(from, to, cost));
        }
        int[] dist = new int[n+1];
        for (int i=1; i<=n; i++) {
            dist[i] = inf;
        }
        dist[1] = 0;
        boolean negative_cycle = false;
        for (int i=1; i<=n; i++) {
            for (Edge e : a) {
                int x = e.from;
                int y = e.to;
                int z = e.cost;
                if (dist[x] != inf && dist[y] > dist[x]+z) {
                    dist[y] = dist[x]+z;
                    if (i == n) {
                        negative_cycle = true;
                    }
                }
            }
        }
        if (negative_cycle) {
            System.out.println("-1");
        } else {
            for (int i=2; i<=n; i++) {
                if (dist[i] == inf) dist[i] = -1;
                System.out.println(dist[i]);
            }
        }
    }
}