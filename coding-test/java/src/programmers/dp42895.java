package programmers;

import java.util.*;

/*
* 프로그래머스 42895번 n 이어 붙이기
* dynamic programming으로 구현
* n번째 시행에서는 시나리오가 다음과 같다.
* 1. dp[1] + dp[n-1], dp[2] + dp[n-2] + ...
* 2. N을 이어붙인 숫자 dp에 더해주기.
* 왜 이렇게 시행되는지에 대해 헷갈렸던 것 같다.
*  */

public class dp42895 {

	class Solution {
		public int solution(int N, int number) {
			List<Set<Long>> dp = new ArrayList<>();
			for (int i = 0; i < 8; i++) {
				dp.add(new HashSet<>());
			}

			if (N == number) {
				return 1;
			}

			dp.get(0).add((long) N);

			String value = String.valueOf(N);
			for (int j = 1; j < 8; j++) {

				StringBuilder sb = new StringBuilder();
				for (int i = 0; i <= j; i++) sb.append(value);
				dp.get(j).add(Long.parseLong(sb.toString()));

				for (int k = 0; k < j; k++) {
					for (long a : dp.get(k)) {
						for (long b : dp.get(j - k - 1)) {
							dp.get(j).add(a + b);
							dp.get(j).add(a - b);
							if (b != 0) {
								dp.get(j).add(a / b);
							}
							dp.get(j).add(a * b);
						}
					}
				}

				for (long comp : dp.get(j)) {
					if (comp == number) {
						return j + 1;
					}
				}
			}

			return -1;
		}
	}

}
