using System;
using System.Collections.Generic;
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
    /// Interaction logic for Credentials.xaml
    /// </summary>
    public partial class CredentialsPage : Page
    {
        public CredentialsPage()
        {
            InitializeComponent();
        }

        private void ExUserPass_Expanded(object sender, RoutedEventArgs e)
        {
            exTrustConnnect.IsExpanded = false;
        }
    }
}
