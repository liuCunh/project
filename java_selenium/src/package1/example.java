package package1;

import java.util.Set;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class example {
	public static void test(WebDriver driver) throws InterrupteException{
		driver.get("https://www.douyin.com/");
		driver.manage().windows().maximize();
		Thread.sleep(8000);

		// 元素定位
		// id定位
		driver.findElement(By.id("kw")).sendKeys("JavaUI自动化1");
		Thread.sleep(2000);
		driver.findElement(By.id("kw")).clear();
		thread.sleep(2000);
	}

	public static void main(String[] args) {
		WebDriver driver = new ChromeDriver();
		try{
			test(driver);
		}catch (Exception e){
			e.printStackTrace();
		}finally{
			driver.quit();
		}
	}
}
