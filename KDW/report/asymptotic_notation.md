## 최악의 경우란?
알고리즘으로 타당하게 문제를 해결하는 방법에는 다양한 방법들이 존재한다. 이 동일한 문제에 한정된 자원으로 적은 비용 즉, **효율성 측면에서 타당한 알고리즘**이 어떤 것인지 중요하다. 
이번 문단에서는 **최악의 수행시간**(크기가 n인 입력 중 가장 오래 걸리는 수행 시간)에 관심을 가질 것이다. 그럼 왜 최악의 수행시간이 중요할까? 이유는 다음과 같다.
- 최악의 경우 수행시간이 모든 수행 시간 중 상한이 된다(이보다 더 나빠질 수 없다.).
- 보통 개발 중 최악의 경우가 빈번히 발생한다(DB에 없는 데이터를 찾는 경우).
- 평균적인 경우가 최악의 경우가 되는 일이 종종 있다.

> 예를 들어, 삽입 정렬을 수행할 떄 입력 크기가 커질 수록 최악의 수행시간이 $O(c_in^2)$이 된다. 
> 여기서, $c_i$는 추상적인 상수를 말한다. 보통 $an^2 + bn + c$로 표현하지만 추상화를 통해 증가 차수를 이용할 수 있다. 이떄, 차수가 가장 높은 항($n^2$)만 고려하고 나머지는 입력의 효율성으로 인해 덜 중요하지기 때문에 최고차항만 남게 되는 것이다. 

## 점근적 표기
알고리즘에서 **점근적(asymptotic)** 이란 의미는 입력이 커지는 경우를 말하며 점근적 분석은 입력 크기가 커질 수록 시간 복잡도 혹은 공간 복잡도가 어떻게 달라지는지 평가하는 것을 말한다. 

![alt text](https://www.boardinfinity.com/blog/content/images/2022/10/o--9-.jpg)

### Θ 표기법
주어진 함수 $g(n)$에 대해 $Θ(g(n))$을 다음과 같이 나타낼 수 있다.

$$
\Theta(g(n)) = \{f(n): \text{모든 } n \geq n_0 \text{에 대해 } 0 \leq c_1 g(n) \leq f(n) \leq c_2 g(n) \text{인 양의 상수 } c_1, c_2, n_0 \text{이 존재한다.}\}
$$

- 이 말은 충분히 큰 n에 대해 f(n)이 두 g(n) 사이에 존재한다면, f(n)이 이 Θ(g(n)) 함수에 속한다는 것이다. 
  - n이 양의 상수 $c_1$과 $c_2$ 사이에 끼여있고 부등식을 만족한다.
  - 이러한 관계를 **점근적으로 정확한 한계(asymptotically tight bound)** 라고 한다.
- 이 식을 정의할 때 반드시 점근적으로 음이 아니다라는 것을 만족해야 한다.
  - $6n^3 \ne Θ(n^2)$ 의 경우 만족할 수 없다.

### O(빅오) 표기법
세타 표기법은 알고리즘의 최대, 최소 수행시간 사이에 수행시간을 표현했다면 빅오 표기법은 **최악의 경우 수행시간** (상한)을 나타낸다. 

$$
O(g(n)) = \{f(n): \text{모든 } n \geq n_0 \text{에 대해 } 0 \leq f(n) \leq cg(n)  {인 양의 상수 } c, n_0 \text{이 존재한다.}\}
$$

- $ g(n)$의 상수배가 $f(n)$이라는 점근적 상한을 의미한다.
- f(n)이 g(n)보다 빠르게 증가하지 않는다. 즉, f(n)은 상한선을 나타낸다. 
- 세타와 빅오의 차이
  - 세타 : 시간 복잡도의 정확성
  - 빅오 : 시간 복잡도의 최악의 경우
  - 세타 표기법은 빅오보다 좀더 엄격한(strict)하다. 즉, 특정 시간 복잡도에 정확히 맞다면 세타 그중 최악이라면 빅오 표기법을 사용한다. 

### Ω(오메가) 표기법
오메가 표기법은 **최소한의 수행시간, 즉 하한**을 표현하는 기법이다.

$$
\Omega(g(n)) = \{f(n): \text{모든 } n \geq n_0 \text{에 대해 } 0 \leq cg(n) \leq f(n)  {인 양의 상수 } c, n_0 \text{이 존재한다.}\}
$$

- 함수 f(n)이 어떤 함수 g(n)의 하한을 나타낸다.  즉, 최소한 이 만큼은 걸린다는 의미이다. 
- 세타 표기법은 상한, 하한선을 동시에 나타내므로 수학적으로 풀이하면 $f(n) = \Theta(g(n))$ 이면 오메가나 빅오나 성립한다는 말이다. 


