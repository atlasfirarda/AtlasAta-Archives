using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media.Imaging;

namespace Default
{
    public partial class MainWindow : Window
    {
        private int currentImage;
        private readonly Uri[] images = new Uri[]
        {
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1740.jpg"),
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1740.png"),
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1739.jpg"),
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1739.png"),
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1737.jpg"),
            new Uri("C:/NextPrevious/Default/Images/IMG_20240302_1737.png")
        };

        private string ImagePath(int imageIndex)
        {
            if(imageIndex == 0)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1740.jpg";
            } else if (imageIndex == 1)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1740.png";
            } else if (imageIndex == 2)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1739.jpg";
            } else if (imageIndex == 3)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1739.png";
            } else if (imageIndex == 4)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1737.jpg";
            } else if (imageIndex == 5)
            {
                return "C:/NextPrevious/Default/Images/IMG_20240302_1737.png";
            }

            return "C:/NextPrevious/Default/Images/IMG_20240302_1740.jpg";
        }

        public MainWindow()
        {
            InitializeComponent();
        }
        
        private bool CanNavigate(bool next)
        {
            if (next && currentImage < images.Length - 1)
                return true;
            else if (!next && currentImage > 0)
                return true;

            return false;
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
                Process.Start(new ProcessStartInfo(@"https://github.com/atlasfirarda")
                {
                    UseShellExecute = true
                });
            }
        }
        
        private void textRClick(object sender, MouseButtonEventArgs e)
        {
            if (e.RightButton == MouseButtonState.Pressed)
            {
                Process.Start(new ProcessStartInfo(@"https://atlasfirarda.carrd.co")
                {
                    UseShellExecute = true
                });
            }
        }
        
        private void ImageBox_Next(object sender, RoutedEventArgs e)
        {
            if (CanNavigate(true))
            {
                currentImage++;
                UpdateImage();
                if (currentImage > 0)
                {
                    PreviousButton.IsEnabled = true;
                }
                if (currentImage == images.Length - 1)
                {
                    NextButton.IsEnabled = false;
                }
            }
        }
        
        private void ImageBox_Previous(object sender, RoutedEventArgs e)
        {
            if (CanNavigate(false))
            {
                currentImage--;
                UpdateImage();
                if (currentImage < 1)
                {
                    PreviousButton.IsEnabled = false;
                }

                if (currentImage < images.Length)
                {
                    NextButton.IsEnabled = true;
                }
            }
        }
        
        private void UpdateImage()
        {
            ImageBox.Source = new BitmapImage(images[currentImage]);
        }

        private void ImageBox_Click(object sender, MouseButtonEventArgs e)
        {
            if (e.LeftButton == MouseButtonState.Pressed && e.ClickCount == 2)
            {
                Process.Start(new ProcessStartInfo(ImagePath(currentImage))
                {
                    UseShellExecute = true
                });
            }
        }
    }
}
