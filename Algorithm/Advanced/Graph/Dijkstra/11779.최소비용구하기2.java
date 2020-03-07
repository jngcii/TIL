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
        int[] dist = new int[n+1];
        boolean[] check = new boolean[n+1];
        int[] from = new int[n+1];
        for (int i=1; i<=n; i++) {
            dist[i] = inf;
            check[i] = false;
        }
        dist[start] = 0;
        from[start] = -1;
        for (int k=0; k<n-1; k++) {
            m = inf+1;
            int x = -1;
            for (int i=1; i<=n; i++) {
                if (check[i] == false && m > dist[i]) {
                    m = dist[i];
                    x = i;
                }
            }
            check[x] = true;
            for (Edge y : a[x]) {
                if (dist[y.to] > dist[x] + y.cost) {
                    dist[y.to] = dist[x] + y.cost;
                    from[y.to] = x;
                }
            }
        }
        System.out.println(dist[end]);
        Stack<Integer> st = new Stack<>();
        int x = end;
        while (x != -1) {
            st.push(x);
            x = from[x];
        }
        System.out.println(st.size());
        while (!st.isEmpty()) {
            System.out.print(st.pop() + " ");
        }
        System.out.println();
    }
}