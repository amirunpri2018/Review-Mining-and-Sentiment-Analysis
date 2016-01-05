import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import com.opencsv.CSVWriter;

public class crawler {

	/**
	 * @param args
	 * @throws IOException 
	 * @throws InterruptedException 
	 */
	public static void main(String[] args) throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		Document doc = null;
		BufferedWriter bw = null;
		// Tab delimited file will be written to data with the name tab-file.csv
		String csv = "C:\\Users\\AshutoshBhargave\\Desktop\\Courses\\Social Media Mining\\Project\\amazon-review.csv";
		CSVWriter writer = new CSVWriter(new FileWriter(csv));
	    //Iterate over all the review pages
		for(int i=1;i<=134;i++)
		{
			if(i%5==0)
			{
				//Thread.sleep(20000);
			}
			System.out.println("Start Again");
			try {
				
				doc =  Jsoup.connect("http://www.amazon.com/Apple-iPhone-16GB-Unlocked-Phone/product-reviews/B00NQGP42Y/ref=cm_cr_pr_btm_link_2?ie=UTF8&showViewpoints=1&sortBy=byRankDescending&pageNumber="+i).timeout(30000).userAgent("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2").get();
						//"http://www.amazon.com/Apple-iPhone-16GB-Unlocked-Phone/product-reviews/B00NQGP42Y/ref=cm_cr_pr_btm_link_2?ie=UTF8&showViewpoints=1&sortBy=byRankDescending&pageNumber="+i).get();
				// http://www.amazon.com/BLU-Advance-Unlocked-Cellphone-White/product-reviews/B00HPTMCRI/ref=cm_cr_pr_btm_link_2?ie=UTF8&showViewpoints=1&sortBy=byRankDescending&pageNumber=
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				Thread.currentThread().sleep(20000);
			}
			//Save the review in the review_title element 
			Elements review_title = doc.select("a[class$=a-size-base a-link-normal review-title a-color-base a-text-bold]");
			Elements review_text = doc.select("span[class$=a-size-base review-text]");
			
			//Save the review author name in review_author element
			Elements review_author = doc.select("a[class$=a-size-base a-link-normal author]");
			//Save the review date in review_date element
			Elements review_date = doc.select("span[class$=a-size-base a-color-secondary review-date]");
			//Save the helpfulness in review_helpfulness 
			Elements review_helpfulness = doc.select("span[class$=a-size-small a-color-secondary review-votes]");
			//Save the ratings in the review_rating
			Elements review_rating = doc.select("span[class$=a-icon-alt]"); 
			
			List title = new ArrayList();
			List text= new ArrayList();
			List rating = new ArrayList();
			List author= new ArrayList();List date= new ArrayList();
			List helpful = new ArrayList();
			for (Element element : review_title) 
			{
				title.add(element.text());
			}
			for (Element element : review_text) 
			{
				text.add(element.text());
			}
			for (Element element : review_author) 
			{
				author.add(element.text());
			}
			for (Element element : review_date) 
			{
				date.add(element.text());
			}
			for (Element element : review_helpfulness) 
			{
				helpful.add(element.text());
			}
			for(Element element : review_rating)
			{
				rating.add(element.text());
			}
			//1 2 3 14 15 16 These indices contain the unnecessary ratings
			System.out.println(rating.size());
			
			rating.remove(0);rating.remove(0);rating.remove(0);
			rating.remove(10);rating.remove(10);rating.remove(10);
			date.remove(0);date.remove(0);
			System.out.println(date);
			System.out.println(rating.size());
			//System.exit(1);
			for(int index=0;index<10;index++)
			{
				//System.out.println(title.get(index));
				//System.out.println(text.get(index));
				//System.out.println(rating.get(index));
				try {
					List<String[]> data = new ArrayList<String[]>();
					try{System.out.println((String) title.get(index));}
					catch (Exception e){title.add(index, "NA");}
					try{System.out.println((String) text.get(index));}
					catch (Exception e){text.add(index, "NA");}
					try{System.out.println((String) rating.get(index));}
					catch (Exception e){rating.add(index, "NA");}
					try{System.out.println((String) author.get(index));}
					catch (Exception e){author.add(index, "NA");}
					try{System.out.println((String) date.get(index));}
					catch (Exception e){date.add(index, "NA");}
					try{System.out.println((String) helpful.get(index));}
					catch (Exception e){helpful.add(index, "NA");}
					data.add(new String[] {(String) title.get(index),(String) text.get(index), (String) rating.get(index),(String) author.get(index),(String) date.get(index),(String) helpful.get(index)});
					writer.writeAll(data);
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}				
			}
		}
		writer.close();
	}

}
