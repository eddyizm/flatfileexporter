using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for AboutPage.xaml
    /// </summary>
    public partial class AboutPage : Page
    {
        public AboutPage()
        {
            InitializeComponent();
        }

        #region Support Links to repo

        private void btnSupportDocs(object sender, RoutedEventArgs e)
        {
            Process.Start("https://bitbucket.org/eddyizm/flatfileexporter/wiki/Home");
            e.Handled = true;
        }

        private void btnIssues(object sender, RoutedEventArgs e)
        {
            Process.Start("https://bitbucket.org/eddyizm/flatfileexporter/issues?status=new&status=open");
            e.Handled = true;
        }

        private void btnCoffee(object sender, RoutedEventArgs e)
        {
            Process.Start("https://ko-fi.com/eddyizm");
            e.Handled = true;
        }

        #endregion

        private void test(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("hello");
        }

        private void Contribute_Expanded(object sender, RoutedEventArgs e)
        {
            CurrentIssues.IsExpanded = false;
        }

    }
}
