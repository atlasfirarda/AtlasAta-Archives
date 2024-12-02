using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace Atlas;

/// <summary>
/// Interaction logic for MainWindow.xaml
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void MainWindow_OnKeyDown(object sender, KeyEventArgs e)
    {
        if (e.Key == Key.Escape)
        {
            this.Close();
        }
    }

    private async void MainWindow_OnLoaded(object sender, RoutedEventArgs e)
    {
        await YoutubeDLSharp.Utils.DownloadYtDlp();
        await YoutubeDLSharp.Utils.DownloadFFmpeg();

    }
    
    private void UIElement_OnMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
    {
        this.DragMove();
    }

    private void ButtonCalcK_OnClick(object sender, RoutedEventArgs e)
    {
        if (ListCalc.Items.Count > 0)
        {
            int lowerThan = ListCalc.Items.Cast<int>().Min();
        
            ListCalc.Items.Clear();
        
            ListCalc.Items.Add(lowerThan.ToString());
        }
    }
    private void ButtonCalcB_OnClick(object sender, RoutedEventArgs e)
    {
        if (ListCalc.Items.Count > 0)
        {
            int greaterThan = ListCalc.Items.Cast<int>().Max();
            
            ListCalc.Items.Clear();
            
            ListCalc.Items.Add(greaterThan.ToString());
        }
    }

    private void Button10S_OnClick(object sender, RoutedEventArgs e)
    {
        Random rand = new Random();
        
        ListCalc.Items.Clear();

        for (int i = 0; i < 10; i++)
        {
            int x = rand.Next(0, 100);
            
            ListCalc.Items.Add(x);
        }
    }

    private void ButtonCalcO_OnClick(object sender, RoutedEventArgs e)
    {
        if (ListCalc.Items.Count > 0)
        {
            double average = ListCalc.Items.Cast<int>().Average();
            
            ListCalc.Items.Clear();
            
            ListCalc.Items.Add(average.ToString("0.00"));
        }
    }
}