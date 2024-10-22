using System.Diagnostics;
using System.Windows;
using System.Windows.Input;
using System.Threading.Tasks;

namespace Default
{
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
        
    }
}