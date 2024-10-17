using System.Diagnostics;
using System.Net.Mime;
using System.Windows;
using System.Windows.Input;
using System.Threading.Tasks;
using System.Windows.Media;

namespace Default
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void WindowDrag(object sender, MouseButtonEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                this.DragMove();
            }
        }
        
        // private bool isMaximized = false;

        // private void WindowDClick(object sender, MouseButtonEventArgs e)
        // {
        //     if (e.ClickCount == 2)
        //     {
        //         if (isMaximized)
        //         {
        //             this.WindowState = WindowState.Normal;
        //             isMaximized = !isMaximized;
        //         }
        //         else
        //         {
        //             this.WindowState = WindowState.Maximized;
        //             isMaximized = !isMaximized;
        //         }
        //     }
        // }

        private void WindowClose(object sender, MouseButtonEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                this.Close();
            }
        }

        private void WindowMinimize(object sender, MouseButtonEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                if (this.WindowState != WindowState.Minimized)
                {
                    this.WindowState = WindowState.Minimized;
                }
            }
        }

        private void faviconLClick(object sender, MouseButtonEventArgs e)
        {
            
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                MessageBox.Show("Version: 0.1\n\n   Up to date!", "AtlasAta's Program", MessageBoxButton.OK, MessageBoxImage.Asterisk);
            }
        }

        private void textLClick(object sender, MouseButtonEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed)
            {
                Process.Start(new ProcessStartInfo(@"https://github.com/atlasfirarda"));
            }
        }
        private void textRClick(object sender, MouseButtonEventArgs e)
        {
            if (e.RightButton == MouseButtonState.Pressed)
            {
                Process.Start(new ProcessStartInfo(@"https://atlasfirarda.carrd.co"));
            }
        }

        private async void calculateLClick(object sender, RoutedEventArgs e)
        {

            if (double.TryParse(TextExam1.Text, out var exam1) && double.TryParse(TextExam2.Text, out var exam2))
            {
                double requiredScore = 50;
                double performanceScore = (requiredScore * 3) - (exam1 + exam2);
                double averageScore = (exam1 + exam2) / 2;
                
                LabelExam1.Visibility = Visibility.Hidden;
                LabelExam2.Visibility = Visibility.Hidden;
                TextExam1.Visibility = Visibility.Hidden;
                TextExam2.Visibility = Visibility.Hidden;
                ButtonCalculate.Visibility = Visibility.Hidden;
                LabelExam1.Content = "Your Average Score;";
                LabelExam2.Content = averageScore.ToString("0.00");
                LabelExam1.Visibility = Visibility.Visible;
                LabelExam2.Visibility = Visibility.Visible;
                    
                await Task.Delay(2000);

                if (averageScore < requiredScore)
                {
                    LabelExam1.Visibility = Visibility.Hidden;
                    LabelExam2.Visibility = Visibility.Hidden;
                    TextExam1.Visibility = Visibility.Hidden;
                    TextExam2.Visibility = Visibility.Hidden;
                    ButtonCalculate.Visibility = Visibility.Hidden;
                    LabelExam1.Content = "You must have performance score;";
                    LabelExam2.Content = performanceScore.ToString("0.00");
                    LabelExam1.Visibility = Visibility.Visible;
                    LabelExam2.Visibility = Visibility.Visible;
                    
                    await Task.Delay(3000);
                    
                }
                else
                {
                    await Task.Delay(750);
                }
                    
                LabelExam1.Visibility = Visibility.Hidden;
                LabelExam2.Visibility = Visibility.Hidden;
                
                LabelExam1.Content = "1st Exam Score";
                LabelExam2.Content = "2nd Exam Score";
                
                TextExam1.Clear();
                TextExam2.Clear();
                
                LabelExam1.Visibility = Visibility.Visible;
                LabelExam2.Visibility = Visibility.Visible;
                TextExam1.Visibility = Visibility.Visible;
                TextExam2.Visibility = Visibility.Visible;
                ButtonCalculate.Visibility = Visibility.Visible;
            }
            else
            {
                MessageBox.Show("Please enter a valid number!", "AtlasAta's Program", MessageBoxButton.OK, MessageBoxImage.Error);
        
                TextExam1.Clear();
                TextExam2.Clear();
            }

        }
        
    }
}
