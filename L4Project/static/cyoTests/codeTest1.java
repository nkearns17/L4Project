import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test the numOnes function
 */
public class codeTest1 {
    
  @Before
  public void setup() {
  }

  @After
  public void teardown() {
  }

  @Test
  public void testZero() {
    int x = cTest.numOnes(0);
    assertTrue("incorrect result (0 should have 0 one bits)", x==0);
  }

  @Test
  public void testOne() {
    int x = cTest.numOnes(1);
    assertTrue("incorrect result (1 should have 1 one bit)", x==1);
  }

  @Test
  public void testPowersOfTwo() {
    // don't go too high or we lose precision
    for (int i=0; i<20; i++) {
      int powerOfTwo = (int)(Math.pow(2,i));
      int x = cTest.numOnes(powerOfTwo);
      assertTrue("incorrect result (any power of 2 should have 1 one bit)", x==1);
    }
  }

  @Test
  public void testMinusOne() {
    int x = cTest.numOnes(-1);
    assertTrue("-1 should have all 32 bits set", x==32);
  }
  
}
