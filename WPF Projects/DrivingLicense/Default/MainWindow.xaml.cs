using System;
using System.Diagnostics;
using System.Net.Mime;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media.Imaging;
using System.Windows.Controls;

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

        private const int CurrentYear = 2024;

        private void RecourseClick(object sender, RoutedEventArgs e)
        {
            if (DatePick.SelectedDate.HasValue && TextID.Text.Length > 0 && double.TryParse(TextID.Text, out double _))
            {
                DateTime selectedDate = DatePick.SelectedDate.Value;
                
                int year = CurrentYear - selectedDate.Year;
                
                if (year >= 100)
                {
                    MessageBox.Show("This people is dead. :P", "AtlasAta's Program", MessageBoxButton.OK, MessageBoxImage.Exclamation);
                    
                    TextID.Clear();
                    DatePick.ClearValue(DatePicker.SelectedDateProperty);
                    ShowAge.Content = "+100";
                }
                else
                {
                    ShowAge.Content = year.ToString();
                }
                

                if (MotoLicense.IsChecked == true)
                {
                    if (year >= 16)
                    {
                        if (!MotoList.Items.Contains(TextID.Text))
                        {
                            MotoList.Items.Add(TextID.Text);
                            TextID.Clear();
                            DatePick.ClearValue(DatePicker.SelectedDateProperty);
                        }
                    }
                    else
                    {
                        MessageBox.Show("This teenager can't get a moto license.", "MotoLicense", MessageBoxButton.OK, MessageBoxImage.Exclamation);
                        TextID.Clear();
                        DatePick.ClearValue(DatePicker.SelectedDateProperty);
                    }
                } else if (CarLicense.IsChecked == true)
                {
                    if (year >= 18)
                    {
                        if (!CarList.Items.Contains(TextID.Text))
                        {
                            CarList.Items.Add(TextID.Text);
                            
                            TextID.Clear();
                            DatePick.ClearValue(DatePicker.SelectedDateProperty);
                        }
                    }
                    else
                    {
                        MessageBox.Show("This teenager can't get a car license.", "CarLicense", MessageBoxButton.OK, MessageBoxImage.Exclamation);
                        TextID.Clear();
                        DatePick.ClearValue(DatePicker.SelectedDateProperty);
                    }
                }
                
            }
            else
            {
                MessageBox.Show("Please enter valid inputs in fields.", "AtlasAta's Program", MessageBoxButton.OK, MessageBoxImage.Error);
                TextID.Clear();
                DatePick.ClearValue(DatePicker.SelectedDateProperty);
            }
        }
    }
}
