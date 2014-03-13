import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test the isPrime function
 */
public class codeTest2 {
    
  @Before
  public void setup() {
  }

  @After
  public void teardown() {
  }

  @Test
  public void testProduct() {
    for (int i=2; i<10; i++) {
      boolean b = cTest.isPrime(i*i);
      assertTrue("incorrect result (square num is not prime)", b==false);
    }
  }

  @Test
  public void testTwo() {
    boolean b = cTest.isPrime(2);
    assertTrue("incorrect result (2 is prime)", b==true);
  }

  @Test
  public void testPrimes() {
    int [] primes = {3, 5, 7, 11, 13, 17, 19, 23};
    for (int prime : primes) {
      boolean b = cTest.isPrime(prime);
      assertTrue("incorrect result (number is prime)", b==true);
    }
  }


}
