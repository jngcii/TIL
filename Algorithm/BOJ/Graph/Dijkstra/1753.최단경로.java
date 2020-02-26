import java.util.*;
class Edge implements Comparable<Edge> {
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
    public int compareTo(Edge that) {
        if (this.cost < that.cost) {
            return -1;
        } else if (this.cost == that.cost) {
            if (this.to < that.to) return -1;
            else if (this.to > that.to) return 1;
            else return 0;
        } else {
            return 1;
        }
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
        int start = sc.nextInt();
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            a[x].add(new Edge(y,z));
        }
        int[] dist = new int[n+1];
        boolean[] check = new boolean[n+1];
        for (int i=1; i<=n; i++) {
            dist[i] = inf;
            check[i] = false;
        }
        dist[start] = 0;
        PriorityQueue<Edge> q = new PriorityQueue<>();
        q.add(new Edge(start, 0));
        while (!q.isEmpty()) {
            int x = q.remove().to;
            if (check[x]) continue;
            check[x] = true;
            for (Edge y : a[x]) {
                if (dist[y.to] > dist[x] + y.cost) {
                    dist[y.to] = dist[x] + y.cost;
                    q.add(new Edge(y.to, dist[y.to]));
                }
            }
        }
        for (int i=1; i<=n; i++) {
            if (dist[i] == inf) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }
    }
}